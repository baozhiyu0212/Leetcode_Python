std::vector<int> incrementalBackups(int lastBackupTime, std::vector<std::vector<int>> changes) {
    unordered_set<int> s;
    map<int,vector<int>> m;
    for(auto i:changes){
        m[i[0]].push_back(i[1]);
    }
    for(auto iter=m.begin();iter!=m.end();iter++){
        if(iter->first>lastBackupTime) {
            for(int j=0;j<iter->second.size();j++){
                s.insert(iter->second[j]);
            }
        }
    }
    vector<int> res(s.begin(),s.end());
    sort(res.begin(),res.end());
    return res;
}
