package grailsproject


/* NOT A REST API YET

import grails.rest.RestfulController

class TextbookController extends RestfulController {

    static allowedMethods = [createAccount: 'POST']
    static responseFormats = ['json', 'xml']

    TextbookController(){
        super(UserAccount)
    }
*/

// Should really be called AccountController but I'm just messing around here
// Just sample code at this point--I'm not sure how authentication will be set up but hopefully we'll know in class
class TextbookController {

    def index() {
        // shows form by rendering textbook/index.gsp page in views
        render (view: "index")
    }


    // createAccount method is executed when form is submitted
    /* In our real implementation, this will be a REST method at a URL that the front end will make requests to.
       For now, though, there's no REST for simplicity
     */
    def createAccount() {
        // get emailAddress from submitted form
        def email = params.emailAddress
        // check if an account with that email exists
        def acc = UserAccount.find{emailAddress == email}
        // if an account with specified email is not in database
        if(acc == null) {
            new UserAccount(emailAddress: email, password: params.password,
                            profile: new Profile(displayName: params.displayName, contactMethod: params.contactMethod)).save()
            // print to console
            println("Account created!")
        }
        // if account already exists
        else {
            // print to console
            println("Cannot create account: username already exists")
        }
    }

    def again() {
        render(view: "index")
    }


}
