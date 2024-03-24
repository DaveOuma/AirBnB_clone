#!/usr/bin/env bash
set -e

# Change directory to the parent directory of the script
cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

# Generate the AUTHORS file
{
    # Header with explanatory comments
    cat <<-EOH
        # This file lists all individuals having contributed content to the repository.
        # For how it is generated, see 'hack/generate-authors.sh'.
	EOH
    echo # Add an empty line

    # Retrieve the commit history and format each commit with the author's name and email
    git log --format='%aN <%aE>' |
    LC_ALL=C.UTF-8 sort -uf
} > AUTHORS

