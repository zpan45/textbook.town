package grails3.example

class Auction {
    int minimumBid          // minimum price seller is willing to sell for
    float salePrice         // actual sale price (can be updated as each bid comes in until deadline)
    boolean isCurrent       // whether or not the auction is active
    Date closingTime        // Groovy Date object for when auction ends

    static hasOne = [textbook: Textbook]

    static hasMany = [bids: Bid]

    static constraints = {
        closingTime nullable: false
        minimumBid nullable: false
        textbook nullable: true         // switch this back to false after testing
        bids nullable: true
    }
}
