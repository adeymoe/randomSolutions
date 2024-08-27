function getAverage(marks){
    //TODO : calculate the downward rounded average of the marks array
    const sum = marks.reduce((a,b)=> a + b, 0)
    
    return Math.floor(sum/marks.length)
  }