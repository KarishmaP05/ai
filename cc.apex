public class Main 
{
    public class OlderAccountsUtility 
    {
        
    public static void update0lderAccounts() 
    
        { // Get the 5 oldest accounts

            Account[] oldAccounts = [SELECT Id, Description FROM Account ORDER BY CreatedDate ASC // loop through them and update the Description field }

            for (Account acct: oldAccounts) 
            {

            acct.Description = "Heritage Account";

            // save the change you made

            update oldAccounts;

            }
        
        }

    }

}
