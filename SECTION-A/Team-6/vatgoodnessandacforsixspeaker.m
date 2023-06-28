clear all;
S=load('sixspeaker.mat');
model2=S.gmmadaptmodel;
initial_utterance_no=1;
SV = rand( 6656  ,1);
SV(:,1)=[];
for i=1: 200
        SVNEW=gmm2sv(model2{i})
        SV=[SV SVNEW];
   
end
X1=SV';
% for i=1:80
%     M{i}=X1(i,:);
% end
% for i=1:80
%     for j=1:80
%         if i==j
%             diss(i,j)=0;
%             diss(j,i)=0;
%         else
%             a=mvs(i,j,M,80);
%             
%             diss(i,j)=a;
%             diss(j,i)=a;
%          end
%     end
% end
% Z=diss;

gnd = [ones(40,1);ones(40,1)*2;ones(30,1)*3;ones(30,1)*4;ones(30,1)*5;ones(30,1)*6]; 
D = pdist(X1,'euclidean');
Z = squareform(D);
 Anorm = 1-((Z - min(Z(:)))/(max(Z(:)) - min(Z(:))));
 [RV,C1,I1,RI]=VATNEW(Anorm);
 figure
imshow(RV);
imwrite(RV,'D:\vatimages\i1.jpg','Quality',100);
I=imread('D:\vatimages\i1.jpg');
vat_goodness(1)=otsunew(I);
for i=1:200
if ((RI(i)>=1) & (RI(i)<=40))
map(i)=1;
elseif ((RI(i)>40) & (RI(i)<=80))
map(i)=2;
elseif ((RI(i)>80) & (RI(i)<=110))
map(i)=3;
elseif ((RI(i)>110) & (RI(i)<=140))
map(i)=4;
elseif ((RI(i)>140) & (RI(i)<=170))
map(i)=5;
elseif ((RI(i)>170) & (RI(i)<=200))
map(i)=6;
end
end
res = bestMap(gnd,map);
AC(1) = length(find(gnd == res))/length(gnd);
MIhat(1) = MutualInfo(gnd,res);
p=pdist(X1,'cosine');
X=squareform(p);
minVal = min(X(:));
maxVal = max(X(:));
norm_data = (X - minVal) / ( maxVal - minVal );
d=norm_data;
[RV,C,I,RI]=VATNEW(d);
figure
imshow(RV);
imwrite(RV,'D:\vatimages\i2.jpg','Quality',100);
I=imread('D:\vatimages\i2.jpg');
vat_goodness(2)=otsunew(I);
 for i=1:200
if ((RI(i)>=1) & (RI(i)<=40))
map(i)=1;
elseif ((RI(i)>40) & (RI(i)<=80))
map(i)=2;
elseif ((RI(i)>80) & (RI(i)<=110))
map(i)=3;
elseif ((RI(i)>110) & (RI(i)<=140))
map(i)=4;
elseif ((RI(i)>140) & (RI(i)<=170))
map(i)=5;
elseif ((RI(i)>170) & (RI(i)<=200))
map(i)=6;
end
end
res = bestMap(gnd,map);
AC(2) = length(find(gnd == res))/length(gnd);
MIhat(2) = MutualInfo(gnd,res);
L = CalculateAffinity(X1);
%  figure,imshow(L,[]), title('Affinity Matrix')
% Compute the Degree matrix
for i=1:size(L,1)
     D(i,i) = sum(L(i,:));
end
for i=1:size(L,1)
    for j=1:size(L,2)
        NL1(i,j) = L(i,j) / (sqrt(D(i,i)) * sqrt(D(j,j)));  
    end
end
[eigVectors,eigValues] = eig(NL1);

% % select k largest eigen vectors
k = 6;
nEigVec = eigVectors(:,(size(eigVectors,1)-(k-1)): size(eigVectors,1));
 for i=1:size(nEigVec,1)
    n = sqrt(sum(nEigVec(i,:).^2));    
    U(i,:) = nEigVec(i,:) ./ n; 
end
 p=pdist(U);
 X=squareform(p);
 minVal = min(X(:));
 maxVal = max(X(:));
 norm_data = (X - minVal) / ( maxVal - minVal );
 d=norm_data;
 [RV,C,I,RI]=VATNEW(d);
 figure
 imshow(RV);
 imwrite(RV,'D:\vatimages\i3.jpg','Quality',100);
 I=imread('D:\vatimages\i3.jpg');
 vat_goodness(3)=otsunew(I);
 for i=1:200
if ((RI(i)>=1) & (RI(i)<=40))
map(i)=1;
elseif ((RI(i)>40) & (RI(i)<=80))
map(i)=2;
elseif ((RI(i)>80) & (RI(i)<=110))
map(i)=3;
elseif ((RI(i)>110) & (RI(i)<=140))
map(i)=4;
elseif ((RI(i)>140) & (RI(i)<=170))
map(i)=5;
elseif ((RI(i)>170) & (RI(i)<=200))
map(i)=6;
end
end
res = bestMap(gnd,map);
AC(3) = length(find(gnd == res))/length(gnd);
MIhat(3) = MutualInfo(gnd,res);
p=pdist(U,'cosine');
 X=squareform(p);
 minVal = min(X(:));
 maxVal = max(X(:));
 norm_data = (X - minVal) / ( maxVal - minVal );
 d1=norm_data;
 [RV,C,I,RI]=VATNEW(d1);
 figure
 imshow(RV);
 imwrite(RV,'D:\vatimages\i4.jpg','Quality',100);
 I=imread('D:\vatimages\i4.jpg');
 vat_goodness(4)=otsunew(I);
 for i=1:200
if ((RI(i)>=1) & (RI(i)<=40))
map(i)=1;
elseif ((RI(i)>40) & (RI(i)<=80))
map(i)=2;
elseif ((RI(i)>80) & (RI(i)<=110))
map(i)=3;
elseif ((RI(i)>110) & (RI(i)<=140))
map(i)=4;
elseif ((RI(i)>140) & (RI(i)<=170))
map(i)=5;
elseif ((RI(i)>170) & (RI(i)<=200))
map(i)=6;
end
end
res = bestMap(gnd,map);
AC(4) = length(find(gnd == res))/length(gnd);
MIhat(4) = MutualInfo(gnd,res);

for i=1:200
    M{i}=X1(i,:);
end
for i=1:200
    for j=1:200
        if i==j
            diss(i,j)=0;
            diss(j,i)=0;
        else
            a=mvs(i,j,M,200);
            
            diss(i,j)=a;
            diss(j,i)=a;
         end
    end
end
Z=diss;
 Anorm = 1-((Z - min(Z(:)))/(max(Z(:)) - min(Z(:))));
 [RV,C1,I1,RI]=VATNEW(Anorm);
 figure
 imshow(RV);
 imwrite(RV,'D:\vatimages\i4.jpg','Quality',100);
 I=imread('D:\vatimages\i4.jpg');
 vat_goodness(5)=otsunew(I);
 for i=1:200
if ((RI(i)>=1) & (RI(i)<=40))
map(i)=1;
elseif ((RI(i)>40) & (RI(i)<=80))
map(i)=2;
elseif ((RI(i)>80) & (RI(i)<=110))
map(i)=3;
elseif ((RI(i)>110) & (RI(i)<=140))
map(i)=4;
elseif ((RI(i)>140) & (RI(i)<=170))
map(i)=5;
elseif ((RI(i)>170) & (RI(i)<=200))
map(i)=6;
end
end
res = bestMap(gnd,map);
AC(5) = length(find(gnd == res))/length(gnd);
MIhat(5) = MutualInfo(gnd,res);
disp(vat_goodness);
 disp('The Clustering Accuracy values are');
disp(AC);
disp('The VAT goodness values are');
disp(vat_goodness);
disp('The nomalized mutual information(NMI) values are');
disp(MIhat);

 
%    Davg=mean(Anorm(:));
%   RV3=Anorm-Davg;
% for ls1 = 1:6
%   [center,U,obj_fcn] = fcm(Anorm,ls1);
%  k=1-((U'*U)/max(U(:)));
%  [RV2,C,I,RI]=VAT(k);
%   DUavg=mean(k(:));
%   RV4=k-DUavg;
%   CosTheta(ls1) = sum(dot(RV3,RV4))/(sqrt(sumsqr(RV3))*sqrt(sumsqr(RV4)));
%   figure
%   imshow(RV2);
% end
% excelfilename='D:/data/datatwoeu.xlsx';
% xlswrite(excelfilename, CosTheta);
%  