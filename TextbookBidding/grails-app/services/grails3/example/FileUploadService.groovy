package grails3.example

import grails.transaction.Transactional
import org.springframework.web.multipart.MultipartFile

@Transactional
class FileUploadService {

    def String uploadFile(MultipartFile file, String name, String destinationDirectory ) {

        def serveletContext = ServletContextHolder.servletContext
        def storagePath = serveletContext.getRealPath( destinationDirectory )

        def storagePathDirectory = new File( storagePath )

        if( !storagePathDirectory.exists() ){
            println("creating directory ${storagePath}")
            if(storagePathDirectory.mkdirs()){
                println "SUCCESS"
            }else{
                println "FAILED"
            }
        }

        // Store file

        if(!file.isEmpty()){
            file.transferTo( new File("${storagePath}/${name}") )
            println("Saved File: ${storagePath}/${name}")
            return "${storagePath}/${name}"
        }else{
            println "File: ${file.inspect()} was empty"
            return null
        }
    }
}
