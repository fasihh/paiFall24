get_grade <- function(score) {
    if (score >= 90)
        return("A")
    else if (score >= 80)
        return("B")
    else if (score >= 70)
        return("C")
    return("Fail")
}

score <- 91
print(paste("Score:", score, " Grade:", get_grade(score)))
