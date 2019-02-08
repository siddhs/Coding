/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    openList = ['(','{','[']
    closeList = [')','}',']']
    list = s.split('')
    stack = []
    if(list.length == 0){
        return true
    }
    else{
        for (i in list){
            if (openList.includes(list[i])){
                stack.push(list[i])
            }
            else if (closeList.includes(list[i])){
                position = closeList.indexOf(list[i])
                if (stack.length > 0 && openList[position] === stack[stack.length-1]){
                    stack.pop()
                }
                else {
                    return false
                }
            }
        }
        if (stack.length == 0) {return true}
        else return false
    }
};
