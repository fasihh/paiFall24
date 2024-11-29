# print(sum(nums[nums %% 2 == 0])) R way of solving it

get_sum_even <- function(nums) {
    sum <- 0
    for (num in nums)
        if (num %% 2 == 0)
            sum <- sum + num
    return(sum)
}

print(get_sum_even(c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

