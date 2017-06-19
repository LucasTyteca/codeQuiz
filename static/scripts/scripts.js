var warningPlayer1 = false;
var warningPlayer2 = false;
var warningPlayer3 = false;
var warningPlayer4 = false;
var warningDisplayName1 = false;
var warningDisplayName2 = false;
var warningDisplayName3 = false;
var warningDisplayName4 = false;

function fillUpInput1(players) {
    var value = document.getElementById("chooseplayer1").value;
    var player2 =  document.getElementById("chooseplayer2").value;
    var player3 =  document.getElementById("chooseplayer3").value;
    var player4 =  document.getElementById("chooseplayer4").value;
    var firstname = document.getElementById("firstname1");
    var lastname = document.getElementById("lastname1");
    var displayname = document.getElementById("displayname1");
    if (value === "newPlayer") {
        firstname.value = "";
        lastname.value = "";
        displayname.value = "";

    } else {
        var player = players[value-1];
        firstname.value = player[2];
        lastname.value = player[3];
        displayname.value = player[1];
    }
    if((value!=player2 && value!=player3 && value!=player4)||(value === "newPlayer")) {
        warningPlayer1 = false;
        document.getElementById("chooseplayer1").style.borderColor = "rgb(169, 169, 169)";
        playerWarning();
    }else{
        warningPlayer1 = true;
        document.getElementById("chooseplayer1").style.borderColor = "red";
        playerWarning();
    }
}

function fillUpInput2(players) {
    var value = document.getElementById("chooseplayer2").value;
    var player1 =  document.getElementById("chooseplayer1").value;
    var player3 =  document.getElementById("chooseplayer3").value;
    var player4 =  document.getElementById("chooseplayer4").value;
    var firstname = document.getElementById("firstname2");
    var lastname = document.getElementById("lastname2");
    var displayname = document.getElementById("displayname2");
    if(value === "newPlayer"){
        firstname.value = "";
        lastname.value = "";
        displayname.value = "";
    } else{
        var player = players[value-1];
        firstname.value = player[2];
        lastname.value = player[3];
        displayname.value = player[1];
    }
    if((value!=player1 && value!=player3 && value!=player4)||(value === "newPlayer")) {
        warningPlayer2 = false;
        document.getElementById("chooseplayer2").style.borderColor = "rgb(169, 169, 169)";
        playerWarning();
    }else{
        warningPlayer2 = true;
        document.getElementById("chooseplayer2").style.borderColor = "red";
        playerWarning();
    }
}

function fillUpInput3(players) {
    var value = document.getElementById("chooseplayer3").value;
    var player1 =  document.getElementById("chooseplayer1").value;
    var player2 =  document.getElementById("chooseplayer2").value;
    var player4 =  document.getElementById("chooseplayer4").value;
    var firstname = document.getElementById("firstname3");
    var lastname = document.getElementById("lastname3");
    var displayname = document.getElementById("displayname3");
    if (value === "newPlayer") {
        firstname.value = "";
        lastname.value = "";
        displayname.value = "";
    } else {
        var player = players[value-1];
        firstname.value = player[2];
        lastname.value = player[3];
        displayname.value = player[1];
    }
    if((value!=player1 && value!=player2 && value!=player4)||(value === "newPlayer")) {
        warningPlayer3 = false;
        document.getElementById("chooseplayer3").style.borderColor = "rgb(169, 169, 169)";
        playerWarning();
    }else{
        warningPlayer3 = true;
        document.getElementById("chooseplayer3").style.borderColor = "red";
        playerWarning();
    }
}

function fillUpInput4(players) {
    var value = document.getElementById("chooseplayer4").value;
    var player1 =  document.getElementById("chooseplayer1").value;
    var player2 =  document.getElementById("chooseplayer2").value;
    var player3 =  document.getElementById("chooseplayer3").value;
    var firstname = document.getElementById("firstname4");
    var lastname = document.getElementById("lastname4");
    var displayname = document.getElementById("displayname4");
    if(value === "newPlayer"){
        firstname.value = "";
        lastname.value = "";
        displayname.value = "";

    } else{
        var player = players[value-1];
        firstname.value = player[2];
        lastname.value = player[3];
        displayname.value = player[1];
    }
    if((value!=player1 && value!=player2 && value!=player3)||(value === "newPlayer")) {
        warningPlayer4 = false;
        document.getElementById("chooseplayer4").style.borderColor = "rgb(169, 169, 169)";
        playerWarning();
    }else{
        warningPlayer4 = true;
        document.getElementById("chooseplayer4").style.borderColor = "red";
        playerWarning();
    }
}

function quizDescription(quizzes) {
    var quizid = document.getElementById("choosequizdrop").value;
    var quiz = quizzes[quizid];
    document.getElementById("quizDescription").innerHTML = quiz[2];
}

function changeDisplayName1(players){
    var displayname = document.getElementById("displayname1");
    var playerid = document.getElementById("chooseplayer1").value;
    if(displayname.value != players[playerid-1][1]) {
        for (i = 0; i < players.length; i++) {
            if (players[i][1] == displayname.value) {
                warningDisplayName1 = true;
                displayname.style.borderColor = "Red";
                displayNameWarning();
                break;
            } else {
                warningDisplayName1 = false;
                displayname.style.borderColor = "initial";
                displayNameWarning();
            }
        }
    }else{
        warningDisplayName1 = false;
        displayname.style.borderColor = "initial";
        displayNameWarning();
    }
}

function changeDisplayName2(players){
    var displayname = document.getElementById("displayname2");
    var playerid = document.getElementById("chooseplayer2").value;
    if(displayname.value != players[playerid-1][1]) {
        for (i = 0; i < players.length; i++) {
            if (players[i][1] == displayname.value) {
                warningDisplayName2 = true;
                displayname.style.borderColor = "Red";
                displayNameWarning();
                break;
            } else {
                warningDisplayName2 = false;
                displayname.style.borderColor = "initial";
                displayNameWarning();
            }
        }
    }else{
        warningDisplayName2 = false;
        displayname.style.borderColor = "initial";
        displayNameWarning();
    }
}

function changeDisplayName3(players){
    var displayname = document.getElementById("displayname3");
    var playerid = document.getElementById("chooseplayer3").value;
    if(displayname.value != players[playerid-1][1]) {
        for (i = 0; i < players.length; i++) {
            if (players[i][1] == displayname.value) {
                warningDisplayName3 = true;
                displayname.style.borderColor = "Red";
                displayNameWarning();
                break;
            } else {
                warningDisplayName3 = false;
                displayname.style.borderColor = "initial";
                displayNameWarning();
            }
        }
    }else{
        warningDisplayName3 = false;
        displayname.style.borderColor = "initial";
        displayNameWarning();
    }
}

function changeDisplayName4(players){
    var displayname = document.getElementById("displayname4");
    var playerid = document.getElementById("chooseplayer4").value;
    if(displayname.value != players[playerid-1][1]) {
        for (i = 0; i < players.length; i++) {
            if (players[i][1] == displayname.value) {
                warningDisplayName4 = true;
                displayname.style.borderColor = "Red";
                displayNameWarning();
                break;
            } else {
                warningDisplayName4 = false;
                displayname.style.borderColor = "initial";
                displayNameWarning();
            }
        }
    }else{
        warningDisplayName4 = false;
        displayname.style.borderColor = "initial";
        displayNameWarning();
    }
}

function playerWarning(){
    if(warningPlayer1==true || warningPlayer2==true || warningPlayer3==true || warningPlayer4==true){
        document.getElementById("playerwarning").style.display = "block";
        displayError();
    }else{
        document.getElementById("playerwarning").style.display = "none";
        displayError();
    }
}

function displayNameWarning(){
    if(warningDisplayName1==true || warningDisplayName2==true || warningDisplayName3==true || warningDisplayName4==true){
        document.getElementById("displaynamewarning").style.display = "block";
        displayError();
    }else {
        document.getElementById("displaynamewarning").style.display = "none";
        displayError();
    }
}

function displayError(){
    var displaynameerror = document.getElementById("displaynamewarning").style.display;
    var playererror = document.getElementById("playerwarning").style.display;
    var error = document.getElementById("warning");
    var button = document.getElementById("submitQuizzen");
    if((displaynameerror == "block") || (playererror == "block")){
        if(displaynameerror=="block" && playererror=="block"){
            document.getElementById("warning").style.lineHeight="29px";
        }else{
            document.getElementById("warning").style.lineHeight="70px";
        }
        error.style.display="block";
        button.disabled=true;

    }else{
        error.style.display = "none";
        button.disabled=false;
    }
}

function changeRadioNewQuiz(xvalue, checked){
    radio1 = xvalue.toString() + xvalue.toString() + "1";
    radio2 = xvalue.toString() + xvalue.toString() + "2";
    radio3 = xvalue.toString() + xvalue.toString() + "3";
    radio4 = xvalue.toString() + xvalue.toString() + "4";

    radio1 = document.getElementById(radio1);
    radio2 = document.getElementById(radio2);
    radio3 = document.getElementById(radio3);
    radio4 = document.getElementById(radio4);

    textid = xvalue.toString() + checked.toString();
    answer = document.getElementById(textid).value;

    if(answer != "") {
        if (checked == 1) {
            radio2.checked = false;
            radio3.checked = false;
            radio4.checked = false;
        } else if (checked == 2) {
            radio1.checked = false;
            radio3.checked = false;
            radio4.checked = false;
        } else if (checked == 3) {
            radio1.checked = false;
            radio2.checked = false;
            radio4.checked = false;
        } else if (checked == 4) {
            radio1.checked = false;
            radio2.checked = false;
            radio3.checked = false;
        }
    }else{
        checkedid = xvalue.toString() + xvalue.toString() + checked.toString();
        document.getElementById(checkedid).checked=false;
    }
}

function checkCorrAnswers(amountQuestions){
    var corr = [];
    for (i = 1; i < amountQuestions; i++) {
loop:
        for (value =1; value <= 4; value++){
            radio = i.toString() + i.toString() + value.toString();
            if(document.getElementById(radio).checked==true){
                corr[i]=true;
                break loop;
            }else{
                corr[i] = false;
            }
        }
    }
    errorfound = false;
    for (i = 1; i < corr.length; i++) {
        warningid = "warning"+ i.toString();
        noCorrAnswerid = "noCorrAnswr" + i.toString();
        if(corr[i]==false){
            document.getElementById(warningid).style.display="block";
            document.getElementById(noCorrAnswerid).style.display="block";
            errorfound=true;
        } else{
            document.getElementById(warningid).style.display="none";
            document.getElementById(noCorrAnswerid).style.display="none";
        }
    }
    if (errorfound == false){
        document.forms["newQuiz"].submit();
    }
}

function buttonCreateNewQuizFunc(){
    amountquestionslength=document.getElementById("amountquestions").value;
    itisanumeber=true;
    for(i=0; i < amountquestionslength.length; i++){
        if(amountquestionslength.charAt(i) >= '0' && amountquestionslength.charAt(i) <= '9'){
            console.log(amountquestionslength.charAt);
            itisanumeber=true;
        }else{
            itisanumeber=false;
            break
        }
    }
    if (amountquestionslength<1){
        itisanumeber = false;
    }
    if(itisanumeber == true){
        document.forms['createNewQuiz'].submit();
    }else{
        document.getElementById("warningNaN").style.display="block";
    }
}

$(document).ready(function(){
    var $menu = $('#menu');
    $('#menu').mmenu({
        "offCanvas": {
            "position" : "top",
            "zposition": "front"
        },
        "navbar": {
            "add": "false"
        },
        "slidingSubmenus": false
    });
    var api = $menu.data("mmenu");

    var $btnmenu = $('#mmenuopen');
    $('#mmenuopen').click(function(){
        api.open();
    });
});