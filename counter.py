import pyTeal from *

handle_creation = Seq(
    App.globalPut(bytes("count"), Int(10))
    Approve()
)

router = Router(
    "Simple Router",
    BareCallActions(
        no_op = OnCompleteActions.create_only(handle_creation)
    )
)

@router.method 
    def increment():
        scratchCount = Scratchvar(TealType.int(4))
        return Seq(
            scratchCount.stare(App.globalGet(Bytes("count"))),
            App.globalPut(Bytes("count"), scratchCount.load() + Int(1))
        )