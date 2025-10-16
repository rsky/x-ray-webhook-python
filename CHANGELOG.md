# Changelog

## 1.0.0 (2025-10-16)

Full Changelog: [v0.11.1...v1.0.0](https://github.com/rsky/x-ray-webhook-python/compare/v0.11.1...v1.0.0)

### ⚠ BREAKING CHANGES

* rename /cahce/invalidate -> /resource/update

### Chores

* **internal:** detect missing future annotations with ruff ([eff8152](https://github.com/rsky/x-ray-webhook-python/commit/eff8152eb8c0292aae77876e1ab90f6a2c5830ac))


### Refactors

* rename /cahce/invalidate -&gt; /resource/update ([2892177](https://github.com/rsky/x-ray-webhook-python/commit/28921771e24f73750ff603a1d70c732a67277e28))

## 0.11.1 (2025-09-20)

Full Changelog: [v0.11.0...v0.11.1](https://github.com/rsky/x-ray-webhook-python/compare/v0.11.0...v0.11.1)

### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([3645265](https://github.com/rsky/x-ray-webhook-python/commit/364526564b9e95e50cc010a3e06ab6c01962c13b))
* **internal:** codegen related update ([d8d7a9f](https://github.com/rsky/x-ray-webhook-python/commit/d8d7a9f7b9ce068997250b0cbf46014ffec2e6f0))
* **internal:** update pydantic dependency ([117eaa7](https://github.com/rsky/x-ray-webhook-python/commit/117eaa7329a5d5652cb817f79b31904426a81a9c))
* **types:** change optional parameter type from NotGiven to Omit ([963f5d3](https://github.com/rsky/x-ray-webhook-python/commit/963f5d3323393aa3da3fdcea631cd281a8371e36))

## 0.11.0 (2025-09-05)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/rsky/x-ray-webhook-python/compare/v0.10.0...v0.11.0)

### Features

* improve future compat with pydantic v3 ([60390e0](https://github.com/rsky/x-ray-webhook-python/commit/60390e0cfeaee7ce6f455f2d6a2277bee5afd209))
* **types:** replace List[str] with SequenceNotStr in params ([522e32c](https://github.com/rsky/x-ray-webhook-python/commit/522e32c1bd25f78f5f4dc954cab5142f074e2a74))


### Chores

* **internal:** add Sequence related utils ([706026c](https://github.com/rsky/x-ray-webhook-python/commit/706026cad12bdb64019990bce917a8aecbbe8032))
* **internal:** move mypy configurations to `pyproject.toml` file ([c0237fe](https://github.com/rsky/x-ray-webhook-python/commit/c0237fe12ab93a0922cffc520095a67d53be5c88))

## 0.10.0 (2025-08-29)

Full Changelog: [v0.9.1...v0.10.0](https://github.com/rsky/x-ray-webhook-python/compare/v0.9.1...v0.10.0)

### Features

* **api:** update via SDK Studio ([36790bf](https://github.com/rsky/x-ray-webhook-python/commit/36790bf3543a83bdecd188a0041f8d4bac023ae7))
* **api:** update via SDK Studio ([6a7c279](https://github.com/rsky/x-ray-webhook-python/commit/6a7c279609077da4af1200da4ffe9c5027154222))
* **api:** update via SDK Studio ([916e06f](https://github.com/rsky/x-ray-webhook-python/commit/916e06f039cef726567ea31f2312b2545abb86a7))
* **api:** update via SDK Studio ([bbf7cca](https://github.com/rsky/x-ray-webhook-python/commit/bbf7cca5919c37c28b46e50ff652b45735521063))
* **api:** update via SDK Studio ([96806b9](https://github.com/rsky/x-ray-webhook-python/commit/96806b9102d7ef26db5fa00919d32e929adfbe74))


### Bug Fixes

* avoid newer type syntax ([da1f68b](https://github.com/rsky/x-ray-webhook-python/commit/da1f68b3a8230a97ab4986fb273c943602f4224b))


### Chores

* **internal:** change ci workflow machines ([9b51692](https://github.com/rsky/x-ray-webhook-python/commit/9b51692a72360907e06d0e4564aa60d52e099069))
* **internal:** update pyright exclude list ([e1aedb9](https://github.com/rsky/x-ray-webhook-python/commit/e1aedb96a55051d1053af48304caa7a4e3818ae2))

## 0.9.1 (2025-08-21)

Full Changelog: [v0.9.0...v0.9.1](https://github.com/rsky/x-ray-webhook-python/compare/v0.9.0...v0.9.1)

### Features

* **api:** update via SDK Studio ([b3044e2](https://github.com/rsky/x-ray-webhook-python/commit/b3044e24f1feda909d0930a261ab36b8085972d8))
* **client:** add follow_redirects request option ([078796c](https://github.com/rsky/x-ray-webhook-python/commit/078796c9280d60feaaffda5844aaa3c1d24b0b55))


### Bug Fixes

* **package:** support direct resource imports ([321d7db](https://github.com/rsky/x-ray-webhook-python/commit/321d7dbd4a3b24385b6a6736bcbe8e2df844f857))
* **perf:** optimize some hot paths ([a73e9eb](https://github.com/rsky/x-ray-webhook-python/commit/a73e9ebc14898c6de937530a1083dbff6bb68452))
* **perf:** skip traversing types for NotGiven values ([39a5f6b](https://github.com/rsky/x-ray-webhook-python/commit/39a5f6bd8615d0db29d0ae571e1bf8f5cb538c74))
* **pydantic v1:** more robust ModelField.annotation check ([d6c8b1b](https://github.com/rsky/x-ray-webhook-python/commit/d6c8b1b93cd75c002e1ca6139c7bb4d3cd48a83b))


### Chores

* broadly detect json family of content-type headers ([50138d9](https://github.com/rsky/x-ray-webhook-python/commit/50138d95e88a8f3ca873fd8809ffd44e159355fa))
* **ci:** add timeout thresholds for CI jobs ([cfa9e54](https://github.com/rsky/x-ray-webhook-python/commit/cfa9e5422a7f6c7f270c7ea360b2bf42d0c36af7))
* **ci:** fix installation instructions ([d77adec](https://github.com/rsky/x-ray-webhook-python/commit/d77adecda9578814a036acf4f7b4005c5db0ec59))
* **ci:** only use depot for staging repos ([ff6c5c9](https://github.com/rsky/x-ray-webhook-python/commit/ff6c5c9e66477bb7e62441e695f00897f5e0cb34))
* **ci:** upload sdks to package manager ([67d973b](https://github.com/rsky/x-ray-webhook-python/commit/67d973bbbe00bb435b97eedd4bd791d613563fc5))
* **client:** minor internal fixes ([a190677](https://github.com/rsky/x-ray-webhook-python/commit/a190677e809444eb05f4859d6aeb45f2f14ac969))
* **docs:** grammar improvements ([9292e0f](https://github.com/rsky/x-ray-webhook-python/commit/9292e0f6fae99def2ff0a875e2bc0fe9d1d0f432))
* **docs:** remove reference to rye shell ([d60d774](https://github.com/rsky/x-ray-webhook-python/commit/d60d774d7d66d0f5c5302a313f34a78b3666b19d))
* **internal:** avoid errors for isinstance checks on proxies ([83682fc](https://github.com/rsky/x-ray-webhook-python/commit/83682fc7daac02b940359ebed5d3f2301dfde83a))
* **internal:** base client updates ([99ac40a](https://github.com/rsky/x-ray-webhook-python/commit/99ac40a87ed8d88e980486b68b02f22d14e5452b))
* **internal:** bump pyright version ([6d18cba](https://github.com/rsky/x-ray-webhook-python/commit/6d18cba29aa220fa046ee96bc00ee8f6a507313a))
* **internal:** codegen related update ([87ce424](https://github.com/rsky/x-ray-webhook-python/commit/87ce42475bffe0c088d8dd90434a561817f527ff))
* **internal:** codegen related update ([12aa295](https://github.com/rsky/x-ray-webhook-python/commit/12aa295c089fe829df2360bf810e896c5b49263b))
* **internal:** fix list file params ([8e384f1](https://github.com/rsky/x-ray-webhook-python/commit/8e384f1e9abc44a5e1cfa93af6e6753f796285d3))
* **internal:** import reformatting ([d6dff3d](https://github.com/rsky/x-ray-webhook-python/commit/d6dff3df219ee222f6fab3a226886bd383bcc6d7))
* **internal:** minor formatting changes ([3080a59](https://github.com/rsky/x-ray-webhook-python/commit/3080a5913f6788a9e167a9df27c1845b0ab3b4a4))
* **internal:** refactor retries to not use recursion ([ce33553](https://github.com/rsky/x-ray-webhook-python/commit/ce3355381e19a8639470df9c84c89b2d5f4ddb6b))
* **internal:** update models test ([2aec093](https://github.com/rsky/x-ray-webhook-python/commit/2aec09363eda87876f7b5dd08014f14518462c20))
* **internal:** update pyright settings ([2738a01](https://github.com/rsky/x-ray-webhook-python/commit/2738a01bdce410ae92ede118eb1b325cacee57bc))
* **internal:** version bump ([37188ac](https://github.com/rsky/x-ray-webhook-python/commit/37188ac318bcfcdb860aa7ebd862e3545c30ff1f))

## 0.9.0 (2025-04-11)

Full Changelog: [v0.1.0-alpha.1...v0.9.0](https://github.com/rsky/x-ray-webhook-python/compare/v0.1.0-alpha.1...v0.9.0)

### Features

* **api:** update via SDK Studio ([8f894e4](https://github.com/rsky/x-ray-webhook-python/commit/8f894e41c9cc3cedd3e77102517eb934284465ef))

## 0.1.0-alpha.1 (2025-04-11)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/rsky/x-ray-webhook-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([7589132](https://github.com/rsky/x-ray-webhook-python/commit/758913224da7f757e79a2b69702e4efe3e657435))
* **api:** update via SDK Studio ([6ad6f7c](https://github.com/rsky/x-ray-webhook-python/commit/6ad6f7c973483b885209d5b9977bb9a5a53bcc44))
* **api:** update via SDK Studio ([70713db](https://github.com/rsky/x-ray-webhook-python/commit/70713db420d314ecc01bd0747de7f87b6e1056d1))
* **api:** update via SDK Studio ([a6e7b8c](https://github.com/rsky/x-ray-webhook-python/commit/a6e7b8c5ad8ddf44d9aead6bae565b7dc0fefe5d))
* **api:** update via SDK Studio ([7ad0931](https://github.com/rsky/x-ray-webhook-python/commit/7ad093103b8806b0ba1a75ffe4f3df2e28b64992))
* **api:** update via SDK Studio ([25fb54d](https://github.com/rsky/x-ray-webhook-python/commit/25fb54d91255fda22726499a4300af346d5f84f6))
* **api:** update via SDK Studio ([b3822f4](https://github.com/rsky/x-ray-webhook-python/commit/b3822f4dc020cb66d86f36f9873db182fccf125c))


### Bug Fixes

* **ci:** ensure pip is always available ([9ed6394](https://github.com/rsky/x-ray-webhook-python/commit/9ed639475e64bd3e15afff796095232f10b646eb))
* **ci:** remove publishing patch ([239f55d](https://github.com/rsky/x-ray-webhook-python/commit/239f55d2b97739a81196c181210d09193a26a862))


### Chores

* fix typos ([e751176](https://github.com/rsky/x-ray-webhook-python/commit/e751176bb041325e27a4d019b02206a72404351d))
* go live ([1f6443d](https://github.com/rsky/x-ray-webhook-python/commit/1f6443ddea144975e7461c2ea1173a237e6e1fd7))
* **internal:** expand CI branch coverage ([ed058d9](https://github.com/rsky/x-ray-webhook-python/commit/ed058d91f5af4352297672612b62d3616a93b026))
* **internal:** reduce CI branch coverage ([31a4cc1](https://github.com/rsky/x-ray-webhook-python/commit/31a4cc18498d4747e232311d52a61045f76a4918))
* **internal:** remove trailing character ([f3fd365](https://github.com/rsky/x-ray-webhook-python/commit/f3fd365c83b4306e982ff8a8e23f45519a149c5a))
* **internal:** slight transform perf improvement ([8624f22](https://github.com/rsky/x-ray-webhook-python/commit/8624f22e40b6de617197458b6da4ab15185bbdc6))
* **tests:** improve enum examples ([5b1e091](https://github.com/rsky/x-ray-webhook-python/commit/5b1e091f45c09c60ff674930b8aecd9e3b6c3385))
