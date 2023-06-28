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
fea=X1;
gnd = [ones(40,1);ones(40,1)*2;ones(30,1)*3;ones(30,1)*4;ones(30,1)*5;ones(30,1)*6]; 
% % Finding goodness by OTSU of VAT
p=pdist(fea);
X=squareform(p);
Z=X;
minVal = min(X(:));
maxVal = max(X(:));
Anorm = (X - minVal) / ( maxVal - minVal );
T=mst_prim(Anorm,fea);
full(T);
figure
res = kmeans(fea,6);
res = bestMap(gnd,res);
AC(1) = length(find(gnd == res))/length(gnd);
MIhat(1) = MutualInfo(gnd,res);
l=1;
t=1;
[m n]=size(Z);
%for k1=2:2
    for k=1:5
    big=-10;
for i=1:m
    for j=1:m
        if T(i,j)>big
            big=T(i,j);
            v=i;
            u=j;
        end
    end
end
T(v,u)=0;
T(u,v)=0;
figure
gplot(T,fea);
E=getEdges(T,'adj');
[S, C] = graphconncomp(T);
ncr=grComp(E,S);
di(t)=dunns(S,Z,ncr);
t=t+1;
    end
res1 = bestMap(gnd,C);
AC(2) = length(find(gnd == res1))/length(gnd);
MIhat(2) = MutualInfo(gnd,res1);
display('The Clustering Accuracy in K-means and MST-based-clustering algorithms are as follows');
display(AC);
display('The Normalized Mutual Information in K-means and MST-based-clustering algorithms are as follows');
display(MIhat);