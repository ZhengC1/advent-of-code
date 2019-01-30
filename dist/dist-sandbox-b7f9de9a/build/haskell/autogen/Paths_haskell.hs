{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
module Paths_haskell (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/Users/chun.zheng/github/haskell/.cabal-sandbox/bin"
libdir     = "/Users/chun.zheng/github/haskell/.cabal-sandbox/lib/x86_64-osx-ghc-8.6.3/haskell-0.1.0.0-GPFlTYBDbw322MJjAa4BSa"
dynlibdir  = "/Users/chun.zheng/github/haskell/.cabal-sandbox/lib/x86_64-osx-ghc-8.6.3"
datadir    = "/Users/chun.zheng/github/haskell/.cabal-sandbox/share/x86_64-osx-ghc-8.6.3/haskell-0.1.0.0"
libexecdir = "/Users/chun.zheng/github/haskell/.cabal-sandbox/libexec/x86_64-osx-ghc-8.6.3/haskell-0.1.0.0"
sysconfdir = "/Users/chun.zheng/github/haskell/.cabal-sandbox/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "haskell_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "haskell_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "haskell_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "haskell_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "haskell_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "haskell_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
