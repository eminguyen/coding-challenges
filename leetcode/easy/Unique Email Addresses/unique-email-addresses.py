# https://leetcode.com/problems/unique-email-addresses/solution/

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emails_dict = {}
        
        for email in emails:
            post_at_sign = email.split('@')[-1]
            pre_at_sign = email.split('@')[0]
            pre_at_sign = pre_at_sign.replace('.', '').split('+')[0]
                    
            email = pre_at_sign + '@' + post_at_sign
            
            if email not in emails_dict:
                emails_dict[email] = 1
                
        return len(emails_dict.keys())
        
