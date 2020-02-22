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

"Show file name in  title bar
set title

" Set tabsstop, softtabs, shiftwidth to be equal
" Filetype different settings for tabs
filetype indent on
autocmd Filetype python setlocal noexpandtab ts=4 sts=4 sw=4

" Set autosyntax detection on/off
:syntax on

"Set screen scrolloff, for scroling fw line of the screen
set scrolloff=4

" Bind HJKL + Ctrl to move betwen the windows
map <c-j> <c-w>j
map <c-k> <c-w>k
map <c-h> <c-w>h
map <c-l> <c-w>l

" keep sellection after moving blocks in visual mode
vnoremap < <gV
vnoremap > >gV 

" Allow wildmeni, after : press tab for autohelp on commands
set wildmenu

" When pasting remember the previous document tags and indents
set paste

" Expand history
set history=250
set undolevels=250

" Higlight current line I'm on
set cursorline

" Leave insert mode on qq 
inore qq <Esc>
