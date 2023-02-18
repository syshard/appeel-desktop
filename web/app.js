eel.expose(pythonSay)
eel.expose(ipLocal)
eel.expose(internet)
eel.expose(username)

let ftpPort=21
let host

function audio(caminho) {
	const audioSrc = caminho;
	const audioElement = new Audio(audioSrc);
	audioElement.play();
}

audio("audios/grito.mp3")

let passwordftp = "syshard12345"

$("#senhaftp").val(passwordftp)

function pythonSay(info) {
	console.log(info)
}

function pythonSay(info) {
	console.log(info)
}

function username(user) {
	console.log(user)
	$("#deviceUser").text(user)
	$("#usuarioftp").val(user)
}

function ipLocal(meuip) {
	console.log(meuip)
	$("#textIP").text(meuip)
	host = meuip
}

function internet(internet) {
	console.log(internet)
	$("#status").text("você está : "+internet)
}
                    
// function cmdMenu(){
//     $(".form_menu").toggleClass('show')
// 	$(".bx-menu").toggleClass('bx-x')
// }

function openFtp(){
    $(".form-ftp").toggleClass('showftp')
    audio("audios/grito.mp3")
}

function closeFtp(){
	eel.closeFtp()
	$(".qrFtp").removeClass('showqrcode')
	openFtp()
}

function showhide() {
  let pswrdField = $("#senhaftp");
  pswrdField.attr("type", pswrdField.attr("type") === "password" ? "text" : "password");
  $(".bx-low-vision").toggleClass("bx-show");
}


function startDevices(){
	eel.displayDevices()    
    audio("audios/grito.mp3")
}

function reboot(){
	eel.reboot()
	audio("audios/grito.mp3")
}

function keyboard(){
	eel.keyboard($('#wordlist').val())
	audio("audios/grito.mp3")
}

function beckup(){
	eel.beckup()
	audio("audios/grito.mp3")
}

function pull(){
	eel.adbpull()
	audio("audios/grito.mp3")
}

async function wifiConnect(){
    let dispositivo = await eel.startdevices($("#meuip").val())()
    if (dispositivo !== "Nenhum dispositivo") {
        $("#conn").html("<strong>" + dispositivo + "</strong>").css("color", "green");
        $("#meuip").val()="";
    } else {
        $("#conn").html("<strong>" + dispositivo + "</strong>").css("color", "red");
    }
}

async function dispositivo() {
    let dispositivo = await eel.verficar()()
    if (dispositivo !== "Nenhum dispositivo") {
        $('#conn').html("<strong>" + dispositivo + "</strong>").css("color", "green");
        $('.formScrcpy').addClass('see')
        $('.formAdb').removeClass('see')
    } else {
        $('#conn').html("<strong>" + dispositivo + "</strong>").css("color", "red");
        $('.formAdb').addClass('see')
        $('.formScrcpy').removeClass('see')
    }
}

async function VservidorFTP() {
    let ftp = await eel.Verif_FTP()()
    if (ftp == "on") {
        $('#ftpLink').html("<strong>Servidor ligado</strong>").css("color", "green");
    } else {
        $('#ftpLink').html("<strong>Servidor desligado</strong>").css("color", "red");
    }
}

//setInterval(VservidorFTP,100)
setInterval(dispositivo,100)


function ftpStart(){
	if ($("#usuarioftp").val() && $("#senhaftp").val()) {

		user = $("#usuarioftp").val() 

		if (user.search( /\s/g ) != -1 )
		{
			alert("Não é permitido espaços no campo usuario\n")
		}	
		else{

			eel.startFtp($("#usuarioftp").val(),$("#senhaftp").val())

			var qrcode = new QRCode(document.getElementById("qrcodeftp"), {
	            width : 100,
	            height : 100
	        });

			qrcode.makeCode("ftp://"+host+":"+ftpPort);

			$(".qrFtp").addClass('showqrcode')
			audio("audios/grito.mp3")

		}
	}
	else{
			alert("campos de configuracao nulos")
	}
}

