get_tax_rate <- function(income) {
    if (income > 10000)
        return(0.2)
    else if (income >= 70000)
        return(0.15)
    else if (income >= 30000)
        return(0.10)
    return(0.00)
}

income <- 120000
print(income * get_tax_rate(income))