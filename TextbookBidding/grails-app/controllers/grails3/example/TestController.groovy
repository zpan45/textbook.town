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


    def viewAccount() {
//        def username = params.username
//        def account = User.findByUsername(username)
//        def profile = account.getProfile()

        def j = [:]
        j['item'] = 'hello'
        j['number'] = 9
        // j['profile'] = profile
        render j as JSON
    }


    def simplejson() {

    }
}
