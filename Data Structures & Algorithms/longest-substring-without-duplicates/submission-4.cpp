class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0) return 0;
        unordered_set<char> charList;
        vector<int> maxSize;
        int l = 0;
        int r = 1;
        charList.insert(s[l]);
        maxSize.push_back(charList.size());
        while(r < s.length()){
            while(charList.find(s[r]) != charList.end()){
                charList.erase(s[l]);
                l++;
            }
            charList.insert(s[r]);
            maxSize.push_back(charList.size());
            r++;
        }
        return *max_element(maxSize.begin(), maxSize.end());
    }
};
