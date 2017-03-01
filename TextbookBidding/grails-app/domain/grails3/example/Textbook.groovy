package grails3.example


class Textbook {

    String title
    String isbn
    String author
    String publisher
    String version
    int condition           // from 0-100
    String course
    String university       // if none specified, default is Western
    String coverPhotoPath
    String bestPhotoPath
    String worstPhotoPath

    
    static belongsTo = [seller: Profile]
    static hasOne = [auction: Auction]

    static constraints = {
        // maybe take these out eventually, they're for testing
        university defaultValue: "'Western'"
        bestPhotoPath defaultValue: "''"
        worstPhotoPath defaultValue: "''"
        version defaultValue: "1"
        isbn defaultValue: "XXX"

    }

}
