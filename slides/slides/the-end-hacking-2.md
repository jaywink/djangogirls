## Some things to hack on pt.2

### Add ordering of posts on different criteria
  * criterias: title, view count, published date (default)
  * add to blog list template: ordering, triggers querystring change
  * add to view ordering saving to session and queryset change
  * tests
    - test new session by default orders by published date
    - test calling view with different querystring produces different ordering
    - test ordering sticks via session
