clear all;
% The following commented code is execute only one time for getting MFCC
%  raw data of wave files

%Design Unisversal Background Model - UBM- from Various Speakers

for t=1:231
    mySourceFile = ['D:/ubmspeakersdata/' int2str(t) '.wav'];
    myTargetFile = ['D:/ubmspeakersdata1/' int2str(t) '.mfc']
    args=['-A -D -T 1 -C ']; 
    config1='D:/HTK-3.4.1/htk/config';
    rv= system([get_htk_path 'HCopy ' args  config1 ' '  mySourceFile ' '  myTargetFile]);
end

fid = fopen( 'results1.txt', 'wt' );
for t=1:231
    mySourceFile = ['D:\ubmspeakersdata1\' int2str(t) '.mfc'];
     fprintf( fid, '%s\n',mySourceFile );
end
 A2='results1.txt';
 g='s12';
 ubmmodel = gmm_em(A2, 64 ,8, 2, 1, g);


%   No_of_Speakers=5;
  No_of_Utterances=170;
args=['-A -D -T 1 -C ']; 
config1='D:/HTK-3.4.1/htk/config';
  for i= 1: No_of_Utterances
    %  for j=1:No_of_Utterances
         mySourceFile = ['D:/speechdatanew/fivespeaker/' int2str(i) '.wav'];
         myTargetFile = ['D:/speechdatanew/fivespeaker/' int2str(i) '.mfc'];
         rv= system([get_htk_path 'HCopy ' args  config1 ' '  mySourceFile ' '  myTargetFile]);
%   %end
  end
   fid = fopen( 'fivespeaker.txt', 'wt' );
for t=1:170
    mySourceFile = ['D:\speechdatanew\fivespeaker\' int2str(t) '.mfc'];
     fprintf( fid, '%s\n',mySourceFile );
end
%     args=['-A -D -T 1 -C ']; 
%      config1='D:/HTK-3.4.1/htk/config';
%      for i=1:101
% 
%           mySourceFile = ['D:/fourspeakersdata/' int2str(i) '.wav'];
%           myTargetFile = ['D:/fourspeakersdata/' int2str(i)  '.mfc'];
%           rv= system([get_htk_path 'HCopy ' args  config1 ' '  mySourceFile ' '  myTargetFile]);
%       end
%  

    A3='fivespeaker.txt';
          config='m';
          g1='fivespeaker';
          for i= 1: 170
                     fid = fopen( 'fivespeaker.txt', 'wt' );
                         targetpath=['D:\speechdatanew\fivespeaker\' int2str(i) '.mfc'];
                         fprintf( fid, '%s\n',targetpath);
                         gmmadaptmodel{i} = mapAdapt(A3, ubmmodel, 10, config, g1);
                         save(g1,'-append');
                   fclose(fid);
            end
    
% 
% 
%      
% 
