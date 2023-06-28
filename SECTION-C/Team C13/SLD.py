import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

model = load_model('mp_hand_gesture')

f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()

    x, y, c = frame.shape

    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(framergb)

    # print(result)
    
    className = ''

    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            prediction = model.predict([landmarks])
            # print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]
    else:
        className = 'No hand is detected'

    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_PLAIN, 
                   2, (255,255,255), 2, cv2.LINE_AA)

    cv2.imshow("SLD OUTPUT", frame) 

    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()

cv2.destroyAllWindows()

#Import the necessary libraries
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#Create the NumPy array for actual and predicted labels.
actual = np.array(['rock', 'smile', 'stop', 'okay', 'fist', 'thumbs down', 'thumbs up', 'peace', 'call me', 'live long', 'okay', 'call me', 'live long', 'fist', 'peace', 'thumbs up', 'rock', 'smile', 'thumbs down', 'stop', 'fist', 'rock', 'thumbs down', 'stop', 'live long', 'call me', 'okay', 'thumbs up', 'smile', 'peace', 'okay', 'live long', 'call me', 'stop', 'smile', 'fist', 'thumbs down', 'thumbs up', 'smile', 'peace', 'okay', 'rock', 'smile', 'stop', 'okay','thumbsup'])
predicted= np.array(['rock','smile','live long', 'okay', 'fist', 'thumbs down', 'peace', 'peace', 'call me', 'stop', 'okay', 'call me', 'live long', 'fist', 'peace', 'call me', 'rock', 'smile', 'thumbs down', 'stop', 'fist', 'rock', 'thumbs down', 'stop', 'stop', 'call me', 'okay', 'thumbs up', 'smile', 'peace', 'okay', 'live long', 'call me', 'stop', 'smile', 'fist', 'thumbs down', 'peace','smile', 'peace', 'okay', 'rock', 'smile', 'livelong', 'okay', 'call me'])

#compute the confusion matrix.
cm = confusion_matrix(actual,predicted)

#Plot the confusion matrix.
sns.heatmap(cm,
			annot=True,
			fmt='g',
			xticklabels=['okay', 'peace', 'thumbs up', 'thumbs down', 'call me', 'stop', 'rock', 'live long', 'fist', 'smile'],
			yticklabels=['okay', 'peace', 'thumbs up', 'thumbs down', 'call me', 'stop', 'rock', 'live long', 'fist', 'smile'])
plt.ylabel('Prediction',fontsize=13)
plt.xlabel('Actual',fontsize=13)
plt.title('SLD Confusion Matrix',fontsize=17)
plt.show()

len(predicted)
