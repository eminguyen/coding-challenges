boolean checkPermutation(String s, String t) {
    if(s.length() != t.length()) return false;

    int[] charCount = new int[128];
    for(int i = 0; i < s.length(); i++ ) {
      charCount[(int) s.charAt(i)]++;
    }

    for(int j = 0; j < t.length(); j++ ) {
      int c = (int) t.charAt(j);
      charCount[c]--;
      if(charCount[c] < 0) {
        return false;
      }
    }
    return true;
  }
