package grailsproject

class Textbook {
    // Insert textbook instance variables here
    static belongsTo = [seller: Profile]
    static hasOne = [auction: Auction]
    
    static constraints = {
    }
}
