function lastSurvivor(letters, coords){
	let arr = [];
	let result = "";
	for(let i = 0; i < letters.length; i++) {
		// 문자열 배열에 넣기
		arr[i] = letters.charAt(i);
	}
	while(coords.length > 0){
		// 숫자 배열이 다 없어질때까지
		let index = coords[0];
		arr.splice(index,1);
		// 숫자배열의 첫번째 숫자 위치에 있는 문자열배열 위치에서 한 개 삭제
		coords.splice(0,1);
		// 숫자배열도 맨앞 하나 삭제
	}
	for(let i = 0; i < arr.length; i++){
		result += arr[i];
		// 문자열 배열 문자열화
	}
	return result;
}