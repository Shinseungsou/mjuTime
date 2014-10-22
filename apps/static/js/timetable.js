
//click lectureList
function tabtab(num) {
	var classTable = document.getElementById("classTT");
	day = classTable.rows[num].cells[9].innerHTML;
	start = classTable.rows[num].cells[10].innerHTML;
	end = classTable.rows[num].cells[11].innerHTML;
	prof = classTable.rows[num].cells[3].innerHTML;
	lecture = classTable.rows[num].cells[6].innerHTML;

	var myTable = document.getElementById("myTT");
	dayNumber = days(day);

	for(var i = 0; i <= end-start; i++){
		for(var j = 0; j <= end-start; j++){

		}
	}


	for(var i = 0; i <= end-start; i++){
		myTable.rows[start - 8 + i].cells[dayNumber].innerHTML = prof + "<br/>" + lecture;
	}
	if(classTable.rows[num + 1].cells[1].innerHTML == classTable.rows[num].cells[1].innerHTML){
		tabtab(num+1);
	}else if(classTable.rows[num - 1].cells[1].innerHTML == classTable.rows[num].cells[1].innerHTML){
		tabtab(num-1);
	}
}


function days (day) {
	if(day == "월"){
		return 1;
	}else if(day == "화"){
		return 2;
	}else if(day == "수"){
		return 3;
	}else if(day == "목"){
		return 4;
	}else if(day == "금"){
		return 5;
	}else if(day == "토"){
		return 6;
	}
}


$(document).ready(function(){
	var open = false;
	$('#help').hide();
	$('#helpBtn').click(function(){
		if(open){
			$('#help').hide();
			open = false;
		}else{
			$('#help').show();
			open = true;
		}
	});
	$('#helpClose').click(function(){
		$('#help').hide();
		open = false;
	});
});