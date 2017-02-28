package grails3.example

import grails.converters.JSON
import grails.plugin.springsecurity.annotation.Secured
import grails.rest.RestfulController

@Secured(['ROLE_USER'])
class FileController extends RestfulController{

    static allowedMethods = ['upload': 'POST']
    static responseFormats = ['json', 'xml']

    FileController() {
        super(User)
    }

    def FileUploadService


    def index() {

    }

    // POST method to receive some info
    // @Secured(['ROLE_USER'])
    def upload() {
        def downloadedFile = request.getFile("file")
        // for some reason params.textName etc. is giving me null, so get the JSON explicitly and access it
        String baseImageName = UUID.randomUUID().toString();
        println(baseImageName)
        // Saving image in a folder assets/channelImage/, in the web-app, with the name: baseImageName
        String fileUploaded = FileUploadService.uploadFile( downloadedFile, "${baseImageName}.jpg", "assets/channelImage/" )
        if( fileUploaded ){
            print("FUCK YEAH")
        }


    }
}
