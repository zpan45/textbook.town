package grails3.example


class AuctionService {

    Date stringToDate(String str) {
        // uses the format strings from Java's SimpleDateFormat
        def mydate = Date.parse("yyyy-MM-dd hh:mm:ss", "2014-04-03 1:23:45")


    }
}
