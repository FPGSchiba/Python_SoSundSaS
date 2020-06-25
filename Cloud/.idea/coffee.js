var your_drink = "Mochito";

var reverse = function(s) {
    return s.split("").reverse().join("");
}

var barista = {
    str1: "ion",
    str2: reverse("rcne"),
    str3: "ypt",
    request: function(prefrence){
        return prefrence + "secret word:" + this.str2+this.str3+this.str1;
    }
};

barista.request(your_drink)