#!/usr/bin/env bash

declare -a results
declare -i PYOPT=1 passed=0 failed=0 exit_code=0
declare COLOR_GREEN='\e[32m' COLOR_RED='\e[91m' COLOR_RESET='\e[39m'
MICROPYTHON="${MICROPYTHON:-../build/unix/micropython}"

print_summary() {
    echo
    echo 'Summary:'
    echo '-------------------'
    printf '%b\n' "${results[@]}"
    if [ $exit_code == 0 ]; then
        echo -e "${COLOR_GREEN}PASSED:${COLOR_RESET} $passed/$num_of_tests tests OK!"
    else
        echo -e "${COLOR_RED}FAILED:${COLOR_RESET} $failed/$num_of_tests tests failed!"
    fi
}

trap 'print_summary; echo -e "${COLOR_RED}Interrupted by user!${COLOR_RESET}"; exit 1' SIGINT

cd $(dirname $0)

# TODO: revert back to unit tests for everything
#[ -z "$*" ] && tests=(test_apps.nem2*.py) || tests=($*)
[ -z "$*" ] && tests=(test_apps.nem2*.py) || tests=($*)

declare -i num_of_tests=${#tests[@]}

for test_case in ${tests[@]}; do
    echo
    if $MICROPYTHON -O$PYOPT $test_case; then
        results+=("${COLOR_GREEN}OK:${COLOR_RESET} $test_case")
        ((passed++))
    else
        results+=("${COLOR_RED}FAIL:${COLOR_RESET} $test_case")
        ((failed++))
        exit_code=1
    fi
done

print_summary
exit $exit_code
