package grails3.example

import grails.converters.JSON
import grails.plugin.springsecurity.annotation.Secured
import grails.rest.RestfulController

class TestController extends RestfulController {

    static responseFormats = ['json', 'xml']

    TestController(){
        super(User)
    }

    def index() {

    }

    // This allows a logged-in user to get a json of a user's profile by specifying username


    @Secured(['ROLE_USER'])
    def viewAccount() {
        def username = params.username
        def account = User.findByUsername(username)
        def profile = account.getProfile()

        def j = [:]
        j['item'] = 'hello'
        j['number'] = 9
        j['profile'] = profile
        render j as JSON
    }



    @Secured(['ROLE_USER'])
    def simplejson() {

    }
    // Shows the basic idea of calling a controller method by URL
    // Security/Authentication will be integrated later.
    def getUserPosts(){
        System.out.println('request received.')
        def uname = params.userName
        def account = UserAccount.find{userName == uname}
        if(account!=null){
            respond account.getProfile().getPosts()
        }
        else{
            response.status = 404
        }
    }
}
