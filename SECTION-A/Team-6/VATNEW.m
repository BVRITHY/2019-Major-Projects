function [RV,C,I,RI]=VATNEW(R);
% Example function call: [DV,I] = VAT(D);
%
% *** Input Parameters ***
% @param R (n*n double): Dissimilarity data input
% 
% *** Output Values ***
% @value RV (n*n double): VAT-reordered dissimilarity data
% @value C (n int): Connection indexes of MST
% @value I (n int): Reordered indexes of R, the input data

[N,M]=size(R);

K=1:N;
J=K;
%P=zeros(1,N);

[y,i]=max(R);
[y,j]=max(y);
I=i(j);
J(I)=[];
[y,j]=min(R(I,J));
I=[I J(j)];
J(J==J(j))=[];
C(1:2)=1;

for r=3:N-1,
    [y,i]=min(R(I,J));
    [y,j]=min(y);
    I=[I J(j)];
    J(J==J(j))=[];
    C(r)=i(j);
end;
[y,i]=min(R(I,J));
I=[I J];
C(N)=i;

for r=1:N,
    RI(I(r))=r;
end;

RV=R(I,I);