module Main where

-- main function -> io unit, something that does IO
main :: IO ()
--main = putStrLn "Hello, Haskell!"
main = do
    -- getLine :: IO String
    a <- getLine
    b <- readLn
    if b > 10 then putStrLn "FooBar"
    else putStrLn "something else"
-- main = getLine >>=
--     \a -> readLn >>=
--         \b -> if b > 10 then putStrLn "FooBar" else putStrLn "something else"

foo :: Integer -> Integer -> String
foo 1 b = show (1 - b)
foo a b = show (a + b)

--data Person = Alex | Chun | Cam
--    deriving (Read, Show)

--instance Show Person where
--    show Alex = "Alex"
--    show Cam = "Cameron"
--    show Chun = "Chun"

data Optional arg = ChunNothing | Chun arg
    deriving (Read, Show)

applyToOptional :: (a -> b) -> Optional a -> Optional b
applyToOptional f ChunNothing = ChunNothing
applyToOptional f (Chun a)    = Chun (f a)

-- applyToOptional (+1) ChunNothing === ChunNothing
-- applyToOptional (+1) (Chun 2) === Chun 3

data SinglyLinkedList arg = EmptyList | LinkedList arg (SinglyLinkedList arg)
    deriving (Read, Show)

-- declare the type and the return
headOfList :: SinglyLinkedList arg -> arg

headOfList EmptyList = error "empty list"
headOfList (LinkedList arg _) = arg

tailOfList :: SinglyLinkedList arg -> SinglyLinkedList arg
tailOfList EmptyList = error "empty list"
tailOfList (LinkedList _ arg) = arg

mylast :: SinglyLinkedList a -> a
mylast EmptyList = error "empty list"
mylast (LinkedList a EmptyList) = a
mylast (LinkedList _ b) = mylast b

appendToList :: SinglyLinkedList argA -> SinglyLinkedList argA -> SinglyLinkedList argA
appendToList EmptyList           ls  = ls
appendToList (LinkedList arg ls) lsb = LinkedList arg (appendToList ls lsb)

instance Functor SinglyLinkedList where
    fmap func EmptyList = EmptyList
    fmap func (LinkedList el ll) = LinkedList (func el) (fmap func ll)


-- LinkList 1 (LinkedList 2 Empty)
-- LL 3 (LL 4 Empty)
-- LL 1 (LL 2 (LL 3 (LL 4 Empty)))
--appendToList arg LinkedList list = LinkedList arg(list)

-- type classes are kinda like interfaces
instance Functor Optional where
    fmap = applyToOptional

instance Applicative Optional where
    pure a = Chun a
    ChunNothing <*> b = ChunNothing
    (Chun f) <*> b = fmap f b

instance Monad Optional where
    ChunNothing >>= f = ChunNothing
    (Chun a) >>= f = f a

myDivide :: Double -> Double -> Optional Double
myDivide _ 0 = ChunNothing
myDivide a b = Chun (a / b)

mfunc :: Double -> Optional Double
mfunc a = myDivide 12 a >>= \a' -> myDivide 3 a'
-- mfunc a = do
--     a' <- myDivide 12 a
--     myDivide 3 a'




