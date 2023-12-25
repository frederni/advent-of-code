package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	// Open files
	input, err := os.Open("1/input1.txt")
	check(err)
	scan := bufio.NewScanner(input)
	var lines []string
	for scan.Scan() {
		lines = append(lines, scan.Text())
	}
	check(scan.Err())

	// Initialize stuff
	var calibration_sum int
	written_num_to_int := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}

	for _, l := range lines {
		for word := range written_num_to_int { // Change written numbers with digits
			re := regexp.MustCompile("(.*?)(" + word + ")(.*?)")
			l = re.ReplaceAllString(l, "${1}"+fmt.Sprint(written_num_to_int[word])+"${3}")
		}
		re_number := regexp.MustCompile("[0-9]")
		match_array := re_number.FindAllString(l, -1)
		var last_index int
		if len(match_array) == 1 {
			last_index = 0
		} else {
			last_index = len(match_array) - 1
		}
		calibration, err := strconv.Atoi(match_array[0] + match_array[last_index])
		check(err)
		fmt.Println(l, match_array[0], match_array[last_index])
		calibration_sum = calibration_sum + calibration
	}
	fmt.Println(calibration_sum)
	calibration_sum = 0

}
