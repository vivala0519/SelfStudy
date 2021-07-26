let str = 'abcde';
let ending = 'cde';
let fir_arr = [];
let sec_arr = [];

for(let i = 0; i < str.length; i++) {
	fir_arr.push(str.charAt(i));
}
for(let i = 0; i < ending.length; i++) {
	sec_arr.push(ending.charAt(i));
}
let i = 1;
while(i != sec_arr.length) {
	if(fir_arr[fir_arr.length-i] == sec_arr[sec_arr.legnth-i]) {
		i++;
		return true;
	}	
	else {
		return false;
		break;
	}
}
for(let i = 1; i <= sec_arr.legnth; i++) {
	if(fir_arr[fir_arr.length-i] == sec_arr[sec_arr.legnth-i]) {
		return true;
	}	
	else {
		return false;
		break;
	}
}