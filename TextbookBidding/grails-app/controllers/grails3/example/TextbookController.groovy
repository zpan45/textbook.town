package grails3.example

import grails.converters.JSON
import grails.plugin.springsecurity.annotation.Secured
import grails.rest.RestfulController

@Secured(['ROLE_USER'])
class TextbookController extends RestfulController{

    static allowedMethods = ['simpleAdd': 'POST']
    static responseFormats = ['json', 'xml']

    TextbookController() {
        super(User)
    }


    def index() {

    }

    // POST method to receive some info
    // @Secured(['ROLE_USER'])
    def simpleAdd() {
        // for some reason params.textName etc. is giving me null, so get the JSON explicitly and access it
        def j = request.JSON
        def name = j['textName']
        def author = j['author']
        def username = j['username']

        println(name)

        def account = User.findByUsername(username)
        def profile = account.getProfile()

        // respond profile

        def resp = [:]
        resp['textbookName'] = name
        resp['author'] = author
        resp['profile'] = profile
        render resp as JSON

    }
}
