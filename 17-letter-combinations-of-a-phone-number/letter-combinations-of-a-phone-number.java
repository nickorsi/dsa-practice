class Solution {
    static Map<String, String> PHONE_DIAL_MAP = new HashMap<> ();
    ArrayList<String> letters = new ArrayList<>();
    ArrayList<String> letterCombos = new ArrayList<>();

    static {
        PHONE_DIAL_MAP.put("2", "abc");
        PHONE_DIAL_MAP.put("3", "def");
        PHONE_DIAL_MAP.put("4", "ghi");
        PHONE_DIAL_MAP.put("5", "jkl");
        PHONE_DIAL_MAP.put("6", "mno");
        PHONE_DIAL_MAP.put("7", "pqrs");
        PHONE_DIAL_MAP.put("8", "tuv");
        PHONE_DIAL_MAP.put("9", "wxyz");
    }

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return letterCombos;
        }

        for (int i = 0; i < digits.length(); i ++) {
            letters.add(PHONE_DIAL_MAP.get(String.valueOf(digits.charAt(i))));
        }
        
        backtrack("", 0);
        return letterCombos;
    }

    public void backtrack(String currString, int i) {
        if (currString.length() == letters.size()) {
            letterCombos.add(currString);
            return;
        }

        String currLetters = letters.get(i);

        for (int j = 0; j < currLetters.length(); j++) {
            String newCurrString = currString + currLetters.charAt(j);
            backtrack(newCurrString, i + 1);
        }

    }


    
}