package grails3.example

import grails.converters.JSON
import grails.plugin.springsecurity.annotation.Secured
import grails.rest.RestfulController

import javax.imageio.ImageIO
import java.io.ByteArrayInputStream;
import sun.misc.BASE64Decoder;


class TextbookController extends RestfulController{

    static allowedMethods = ['testing': 'POST','simpleAdd': 'POST']
    static responseFormats = ['json', 'xml']

    TextbookController() {
        super(User)
    }

    def springSecurityService

    def index() {

    }

    // POST method to receive some info
    // @Secured(['ROLE_USER'])
    def testing() {
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

    @Secured(['ROLE_USER'])
    def simpleAdd() {
        // get the current user
        def user = springSecurityService.currentUser
        print(user.id)

        def account = User.findById(user.id)
        def profile = account.getProfile()
        print(profile.displayName)

        def textbook = new Textbook(title: 'Flusharts Explained', author: 'ElSakka', publisher: "Bleh",
                condition: 80, course: 'CS2208', coverPhotoPath: 'nopath').save(flush:true)

//        profile.textbooks.add(new Textbook(title: 'Flusharts Explained', author: 'ElSakka', publisher: "Bleh",
//                condition: 80, course: 'CS2208', coverPhotoPath: 'nopath').save())
//        profile.save()

        def resp = [:]
        resp['status'] = 'success'

        render resp as JSON


        // render resp as JSON
//
//        def j = request.JSON
//        def name = j['textName']
//        def author = j['author']
//        def username = j['username']
//
//        println(name)
//
//        def account = User.findByUsername(username)
//        def profile = account.getProfile()
//
//        // respond profile
//
//        def resp = [:]
//        resp['textbookName'] = name
//        resp['author'] = author
//        resp['profile'] = profile
//        render resp as JSON

    }


}
