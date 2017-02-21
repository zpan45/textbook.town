package grails3.example


class Textbook {

    String title
    String isbn
    String author
    String publisher
    String version
    int condition           // from 1-100
    String course
    String university       // if none specified, default is Western

    
    static belongsTo = [seller: Profile]
    static hasOne = [auction: Auction]

    static constraints = {
        university defaultValue: "'Western'"
    }

}
