# invoke mirror

Mirror of the invoke package for pre-commit

For pre-commit: see https://github.com/pre-commit/pre-commit

Fox invoke: https://github.com/pyinvoke/invoke/


### Using invoke with pre-commit

Add this to your `.pre-commit-config.yaml`:

    -   repo: https://github.com/saltstack/invoke-pre-commit
        rev: ''  # Use the sha / tag you want to point at
        hooks:
        -   id: invoke
            alias: check-docs
            name: Check Docs
            files: ^(salt/.*\.py|doc/ref/.*\.rst)$
            args:
              - docs.check
