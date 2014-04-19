my_tr_data_asym(1,length) = struct('am',[],'nl',struct('values',[]));
my_tr_data_sym(1,length) = struct('am',[],'nl',struct('values',[]));
%asym
basepath_asym = './asym/am_asym/';
basepath_label_asym = './asym/label_asym/';
basepath_al_asym = './asym/al_asym/';
fullpath = '';

for i = 1:length
    fullpath = strcat(basepath_asym,num2str(i-1));
    my_tr_data_asym(i).am = load(fullpath);
    fullpath = strcat(basepath_label_asym,num2str(i-1));
    my_tr_data_asym(i).nl.values = load(fullpath);
    fullpath = strcat(basepath_al_asym,num2str(i-1));
    fin = fopen(fullpath,'r');
    s_in = fgetl(fin);
    counter = 1;
    while s_in ~= -1
        my_tr_data_asym(i).al{counter,1} = str2num(s_in);
        counter = counter+1;
        s_in = fgetl(fin);
    end
    fclose(fin);
end

%sym
%my_tr_data_sym(1,length) = struct('am',[],'nl',struct('values',[]));
basepath_sym = './sym/am_sym/';
basepath_label_sym = './sym/label_sym/';
basepath_al_sym = './sym/al_sym/';
fullpath = '';
for i = 1:length
    fullpath = strcat(basepath_sym,num2str(i-1));
    my_tr_data_sym(i).am = load(fullpath);
    fullpath = strcat(basepath_label_sym,num2str(i-1));
    my_tr_data_sym(i).nl.values = load(fullpath);
    fullpath = strcat(basepath_al_sym,num2str(i-1));
    fin = fopen(fullpath,'r');
    s_in = fgetl(fin);
    counter = 1;
    while s_in ~= -1
        my_tr_data_sym(i).al{counter,1} = str2num(s_in);
        counter = counter+1;
        s_in = fgetl(fin);
    end
    fclose(fin);
end

% load('/Users/Milannic/Dropbox/project/nlp/data/test_tag.mat')
% length = size(test_tag,1);
% my_test_data(1,length) = struct('am',[]);
% basepath = '/Users/Milannic/Dropbox/project/nlp/data/output_test/';
% for i = 1:length
%     fullpath = strcat(basepath,num2str(i-1));
%     my_test_data(i).am = load(fullpath);
% end
