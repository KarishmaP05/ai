public class OlderAccountsUtility{
public static void updateolderAccounts(){

        Account[] oldAccounts= [SELECT Id,Description FROM Account ORDER By CreatedDate ASC LIMIT 5];

        for (Account acct : oldAccounts){

            acct.Description='Heritage Account';

            

        }

        update oldAccounts;

    }

}
    


