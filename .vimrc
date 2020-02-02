" First vimrc file made by Piotr Lenartowicz
" 29.12.2019

" Turn on line numbers on start-up
" Turn the relative numbers
:set nu
:set relativenumber

" Set Default Search highlighting ON
:set hlsearch
:set incsearch 
" Set highlighting OFF
":set noincsearch
":set nohsearch

"Change the unicode character on option list
" The tab character → unicode:u2192 update by pressing ctrl+v and code
" The end of line character ↲ unicode:u21b2 update by presing ctrl+v and code
set listchars=tab:→\ ,eol:↲

" Set tabsstop, softtabs, shiftwidth to be equal
" Filetype different settings for tabs
filetype indent on
autocmd Filetype python setlocal noexpandtab ts=4 sts=4 sw=4

" Leave insert mode on ii
inore ii <Esc>
