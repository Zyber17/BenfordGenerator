function benfordWrapper(digits) {
	num = 0;
	for (var i = 1; i < digits + 1; i++) {
		num += benford(i) * Math.pow(10,digits - i);
	}
	return num;
}

function benford(digit) {
	dist = [0,0,0,0,0,0,0,0,0,0]

	if (digit == 1) {
		for (var i = 1; i < 10; i++) {
			dist[i] = Math.log10(1 + 1/i);

		}
	} else {
		for (var i = 0; i < 10; i++) {
			for (var j = Math.pow(10,digit - 2); j < Math.pow(10,digit - 1); j++) {
				dist[i] += Math.log10(1 + 1/(10 * j + i));
			}
		}
	}
	rand = Math.random();
	numsum = dist[0];
	i = 0;
	while (rand > numsum) {
		i++;
		numsum += dist[i];
	}
	return i;
}


//In case Math.log10 isn't supported in the user's browser
Math.log10 = Math.log10 || function(x) {
  return Math.log(x) / Math.LN10;
};
