import Data.List

answer :: [String] -> Int
answer [x] = (read (filter (/='+') x) :: Int)
answer (x:xs) = 0 + (read (filter (/='+') x) :: Int) + (answer xs)

main = do
    src <- readFile "/Users/chun.zheng/github/haskell/advent/day1/input"
    let l = (lines src)
    print l
    print(answer l)

