clear all, fclose all
fid = fopen('testpaul.csv','r');
A=fscanf(fid,'%f, %f',[2 11])
B = A'
fclose(fid);

x = B(:,1);
y = B(:,2);

