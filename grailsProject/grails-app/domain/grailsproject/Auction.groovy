package grailsproject

class Auction {
    int minimumBid
    float salePrice
    // Need an instance variable for closing date and time

    static hasOne = [textbook: Textbook]

    static hasMany = [bids: Bid]

    static constraints = {
    }
}
