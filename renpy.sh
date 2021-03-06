#!/bin/sh

# The directory containing this shell script - an absolute path.
ROOT=$(dirname "$0")
ROOT=$(cd "$ROOT"; pwd)

# The name of this shell script without the .sh on the end.
BASEFILE=$(basename "$0" .sh)

if [ -z "$RENPY_PLATFORM" ] ; then
    case "$(uname -s)-$(uname -m)" in
        Darwin-*)
            RENPY_PLATFORM="darwin-x86_64"
            ROOT1="$ROOT/../Resources/autorun"
            ROOT2="$ROOT/../../.."
                        ;;        
        *-x86_64|amd64)
            RENPY_PLATFORM="linux-x86_64"
            ROOT1="$ROOT"
            ROOT2="$ROOT"
                        ;;
        *-i*86)
            RENPY_PLATFORM="linux-i686"
            ROOT1="$ROOT"
            ROOT2="$ROOT"
            ;;
        *)
            echo "Ren'Py could not detect that platform it's running on. Please set"
            echo "the RENPY_PLATFORM environment variable to one of \"linux-i686\" or"
            echo "\"linux-x86_64\", or \"darwin-x86_64\" and run this command again."
            exit 1
            ;;
    esac
fi


for BASE in "$ROOT" "$ROOT1" "$ROOT2"; do 
    LIB="$BASE/lib/$RENPY_PLATFORM"
		if test -d "$LIB"; then
		    break
		fi
done

exec $RENPY_GDB "$LIB/$BASEFILE" $RENPY_PYARGS -EOO "$BASE/$BASEFILE.py" "$@"
