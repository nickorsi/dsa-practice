import "fmt"
func isPalindrome(x int) bool {
    strX := fmt.Sprint(x)

    if len(strX) <= 1 {
        return true
    }

    for i := range len(strX) {
        if i == len(strX) - 1 - i {
            return true
        }
        if strX[i] != strX[len(strX) - 1 - i] {
            return false
        }
    }

    return true
}