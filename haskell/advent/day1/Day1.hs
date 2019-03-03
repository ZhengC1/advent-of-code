import Data.List

convertToInt :: String -> Int
convertToInt x = (read (filter (/='+') x) :: Int)

answer :: [String] -> Int
answer [x] = convertToInt x
answer (x:xs) = 0 + convertToInt x + answer xs

convertToIntList :: [String] -> [Int]
convertToIntList [x] = convertToInt x : []
convertToIntList (x:xs) = (convertToInt x) : (convertToIntList xs)

repeatingNum :: Int -> [Int] -> Int
repeatingNum x [x] = error "no repeating num found"
repeatingNum x y = splitAt x y

numInList :: Int -> [Int] -> Bool
numInList x l = x `elem` l

main = do
    src <- readFile "input"
    let l = (lines src)
    print (convertToIntList l)
    print (repeatingNum 1 (convertToIntList l))

