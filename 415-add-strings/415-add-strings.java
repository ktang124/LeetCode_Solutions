class Solution {
    public String addStrings(String num1, String num2) {
       StringBuffer res = new StringBuffer();
        
        int i1 = num1.length() - 1;
        int i2 = num2.length() - 1;
        boolean carry = false;
       
        while(i1 >= 0  || i2 >= 0){
            int cur = 0;
            if(i1 >= 0 && i2 >= 0){
                cur = (int)(num1.charAt(i1) - '0');
                cur += (int)(num2.charAt(i2) -'0');
                if(carry) cur += 1;
                carry = false;
                if(cur > 9) carry = true;
                res.append(cur% 10);
                i1--;
                i2--;
            }else if(i1 >= 0){
                cur = (int)(num1.charAt(i1) - '0');
                if(carry) cur += 1;
                carry = false;
                if(cur > 9) carry = true;
                 res.append(cur % 10);
                i1--;
            }else{
                cur = (int)(num2.charAt(i2) - '0');
                if(carry) cur += 1;
                carry = false;
                if(cur > 9) carry = true;
                 res.append(cur % 10);
                i2--;
            }
        }
        if(carry) res.append(1);
        return res.reverse().toString();
    }
}